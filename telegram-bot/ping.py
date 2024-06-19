import subprocess

def check(host):
    result = ""
    try:
        # ping 명령을 실행하고 결과를 캡처
        run_command = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 결과 출력
        if not run_command.stderr:
            result = run_command.stdout
        else: 
            result = f"{host} is wrong type"


    except Exception as e:
        result = f"An error occurred: {e}"

    return result

if __name__ == "__main__":
    host = input("Enter the host to ping: ")
    print(check(host))
