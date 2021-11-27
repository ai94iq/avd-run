from subprocess import PIPE, Popen

process = Popen( "emulator -list-avds", shell=True, stdout=PIPE,)
stdout, stderr = process.communicate()
print(stdout.decode())

avd = input("Enter AVD name to run: ")
avdrun =  Popen( f"emulator -avd {avd}", shell=True, stdout=PIPE,)