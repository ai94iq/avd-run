from subprocess import PIPE, Popen

process = Popen(
            "emulator -list-avds",
            shell=True,
            stdout=PIPE,
        )
stdout, stderr = process.communicate()
print(stdout.decode())