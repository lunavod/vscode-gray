import subprocess

with subprocess.Popen(
    ['python', '-m', 'gray_formatter', '-'],
    encoding="utf-8",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE
) as process:
    with open('example.py', 'r') as f:
        source = f.read()
    print(process.communicate(input=source))