# deploy.py
import paramiko

def deploy_web_app(server_ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server_ip, username=username, password=password)

        # Step 1: Copy the application code to the server
        sftp = ssh.open_sftp()
        sftp.put('app.py', '/path/to/remote/app.py')
        sftp.close()

        # Step 2: Install dependencies (for example, Flask) on the server
        stdin, stdout, stderr = ssh.exec_command('pip install Flask')

        # Step 3: Start the web application on the server
        stdin, stdout, stderr = ssh.exec_command('python /path/to/remote/app.py &')

        print("Web application deployed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        ssh.close()

if __name__ == '__main__':
    server_ip = 'YOUR_SERVER_IP'
    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'
    deploy_web_app(server_ip, username, password)
