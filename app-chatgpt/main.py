import openai 
import config
import typer
from rich import print
from rich.table import Table


def main():
    client = openai.OpenAI(
        api_key = config.api_key
    )

    print("[bold blue]ChatGPT API en python[/bold blue]")

    table = Table("Comando", "Descripcion")
    table.add_row("exit", "Salir de la aplicacion")
    table.add_row("new", "Crear una nueva conversacion")

    print(table)
    

    #Context of the assistant
    ChatGPT_role=input(" What use do you want to give to chatgpt?")
    Context= {"role": "system", "content": "you are a useful asssitant"}
    message=[Context] 

    while True:
        content=__prompt()

        message.append({
                "role": "user",
                "content": content,
            })
    

        if content == "new":
            message = [Context] 
            print("[green] nueva conversacion[/green]")
            content=__prompt()
            

        response = client.chat.completions.create(
            messages=message,
            model="gpt-3.5-turbo"
        )
        response_content = response.choices[0].message.content
        message.append({
                "role": "assistant",
                "content": response_content,
            })

        print(f"[green]{response_content}[/green]")

def __prompt() -> str:
    prompt=typer.prompt("What do you want to say to ChatGPT? ")

    if prompt == "exit":
        exit = typer.confirm("Are you sure? ")
        if exit:
            print("¡Hasta luego!")
            raise typer.Abort()
        return __prompt
    
    return prompt


if  __name__ == "__main__":
    typer.run(main)