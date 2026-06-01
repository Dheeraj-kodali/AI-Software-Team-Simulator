import os

def save_output(project_name, content):

    print("SAVE_OUTPUT FUNCTION CALLED")

    os.makedirs("outputs", exist_ok=True)

    filename = project_name.replace(" ", "_")

    path = f"outputs/{filename}.txt"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print("FILE SAVED SUCCESSFULLY")
    print(path)

    return path