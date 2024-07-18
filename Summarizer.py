import click
import requests
import json

@click.command()
@click.option('--file', '-t', type=click.File('r'), help='Path to the text file.')
@click.argument('text', nargs=-1, default=None)
def summarize(file, text):
    
    if file:
        text = file.read()
        click.echo(f"Summary of {file.name}:")
    elif text:
        text = ' '.join(text)
        click.echo("Summary of text pasted:")
    else:
        click.echo("Error: Please provide either a file or text.")
        return

    url = "http://localhost:11434/api/generate"
    headers = {'Content-Type': 'application/json'}

    data = {
        "model": "qwen2:0.5b",  # Qwen2 0.5B model
        "prompt": f"Summarize this text: \n{text}",
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        summary = response_json["response"]
        click.echo(summary)
    else:
        click.echo(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    summarize()