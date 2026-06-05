from llm import get_llm
import time


class AISDK:

    total_calls = 0

    @staticmethod
    def generate(prompt, agent_name="Unknown"):

        AISDK.total_calls += 1

        llm = get_llm()

        print(f"\n===== {agent_name} Started =====")

        print(
            f"Prompt Length: {len(prompt)} characters"
        )

        start = time.time()

        response = llm.invoke(prompt)

        end = time.time()

        print(
            f"{agent_name} Finished in {round(end-start, 2)} sec"
        )

        print(
            f"Response Length: {len(response.content)} characters"
        )

        print(
            f"Estimated Tokens: {(len(prompt)+len(response.content))//4}"
        )

        return response.content

    @staticmethod
    def summarize(text):

        llm = get_llm()

        print("\n===== Summary Agent Started =====")

        prompt = f"""
        Summarize the following content.

        Keep only the most important information.

        Maximum 150 words.

        Content:

        {text}
        """

        response = llm.invoke(prompt)

        print("===== Summary Agent Finished =====")

        return response.content