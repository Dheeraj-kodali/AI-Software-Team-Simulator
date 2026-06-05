from langchain_groq import ChatGroq
from pydantic import SecretStr
import groq

from sdk.key_manager import get_current_key, report_usage, get_next_key


class RotatingChatGroq(ChatGroq):

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        # Dynamically fetch the current key
        api_key = get_current_key()

        # Update the API key representation
        self.groq_api_key = SecretStr(api_key)

        # Rebuild clients to use the new key
        self.client = groq.Groq(
            api_key=api_key,
            base_url=self.groq_api_base,
        ).chat.completions

        self.async_client = groq.AsyncGroq(
            api_key=api_key,
            base_url=self.groq_api_base,
        ).chat.completions

        # Generate response
        res = super()._generate(messages, stop=stop, run_manager=run_manager, **kwargs)

        # Extract token usage
        if res.llm_output and "token_usage" in res.llm_output:
            token_usage = res.llm_output["token_usage"]
            total_tokens = token_usage.get("total_tokens", 0)
            report_usage(total_tokens)

        return res

    async def _agenerate(self, messages, stop=None, run_manager=None, **kwargs):
        # Dynamically fetch the current key
        api_key = get_current_key()

        # Update the API key representation
        self.groq_api_key = SecretStr(api_key)

        # Rebuild clients to use the new key
        self.client = groq.Groq(
            api_key=api_key,
            base_url=self.groq_api_base,
        ).chat.completions

        self.async_client = groq.AsyncGroq(
            api_key=api_key,
            base_url=self.groq_api_base,
        ).chat.completions

        # Generate response
        res = await super()._agenerate(messages, stop=stop, run_manager=run_manager, **kwargs)

        # Extract token usage
        if res.llm_output and "token_usage" in res.llm_output:
            token_usage = res.llm_output["token_usage"]
            total_tokens = token_usage.get("total_tokens", 0)
            report_usage(total_tokens)

        return res


def get_llm():

    return RotatingChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=get_current_key(),
        temperature=0.2
    )


llm = get_llm()