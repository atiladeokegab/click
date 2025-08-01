import click
import time
from pathlib import Path
import getpass
import os

@click.group()
@click.version_option("1.0.0", prog_name="click-cli-tool")
def cli():
    """🛠️ A multi-feature Click CLI tool example."""
    pass

# ---------------------------
# Argument, Option, Flag
# ---------------------------
@cli.command()
@click.argument('name')
@click.option('--greeting', default='Hello', help='Greeting to use.')
@click.option('--shout', is_flag=True, help='Shout the greeting.')
def greet(name, greeting, shout):
    """Greet someone with a custom message."""
    msg = f"{greeting}, {name}!"
    if shout:
        msg = msg.upper()
    click.secho(msg, fg='green' if not shout else 'red', bold=True)

# ---------------------------
# Prompt with password confirmation
# ---------------------------
@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def login(username, password):
    """Simulate a login flow."""
    click.echo(f"✅ Logged in as {username}")

# ---------------------------
# Progress bar example
# ---------------------------
@cli.command()
def download():
    """Simulate a download with progress bar."""
    click.echo("Starting download...")
    with click.progressbar(range(100), label="Downloading") as bar:
        for _ in bar:
            time.sleep(0.01)
    click.secho("Download complete!", fg="cyan")

# ---------------------------
# Choice option
# ---------------------------
@cli.command()
@click.option('--level', type=click.Choice(['low', 'medium', 'high']), default='medium')
def risk(level):
    """Print selected risk level."""
    click.echo(f"Risk level set to: {level}")

# ---------------------------
# Read file using pathlib.Path
# ---------------------------
@cli.command()
@click.argument('filepath', type=click.Path(exists=True, path_type=Path))
def read(filepath: Path):
    """Read a file using pathlib."""
    click.echo(f"📄 Reading from: {filepath}\n")
    content = filepath.read_text()
    click.echo(content)

# ---------------------------
# Confirm + styled output
# ---------------------------
@cli.command()
def delete():
    """Ask before deleting (simulated)."""
    if click.confirm("Are you sure you want to delete everything?", abort=True):
        click.secho("🔥 Everything deleted (just kidding).", fg="red", bold=True)

# ---------------------------
# Show system user using pathlib
# ---------------------------
@cli.command()
def whoami():
    """Show the current system user using pathlib & env vars."""
    user = os.getenv("USER") or os.getenv("USERNAME") or getpass.getuser()
    click.echo(f"👤 Current user: {user}")

# ---------------------------
# Chained commands example
# ---------------------------
@cli.group(chain=True)
def batch():
    """Run multiple tasks in one go."""
    pass

@batch.command()
def task1():
    click.echo("✅ Task 1 complete")

@batch.command()
def task2():
    click.echo("✅ Task 2 complete")

# ---------------------------
# Entry point
# ---------------------------
if __name__ == '__main__':
    cli()

def main():
    print("Hello from click-cli-tool!")


if __name__ == "__main__":
    main()
