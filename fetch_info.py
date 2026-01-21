import click
import requests


@click.command()
@click.option("--name", default="", help="User name")
def fetch_n_display(name: str):
    resp = requests.get(f"https://api.github.com/users/{name}/events")

    if resp.status_code == 200:
        respJson = resp.json()

        if not respJson:
            print(f"\nThe user {name} has had no public activity in the past 30 days!")
        else:
            actions = {}

            for i in range(len(respJson)):
                type = respJson[i].get("type")
                if type not in actions:
                    actions[type] = 0

                actions[type] += 1

            print(f"\nThe user {name} has: ")
            for key, value in actions.items():
                print(f"    {value} {key}")

            print()
    else:
        print(f"Error: {resp.status_code}")


if __name__ == "__main__":
    fetch_n_display()
