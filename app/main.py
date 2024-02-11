from fastapi import FastAPI, HTTPException
import docker

app = FastAPI()
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

def check_container_status(container_name):
    try:
        container = client.containers.get(container_name)
        if container.status == 'running':
            return True
        else:
            return False
    except docker.errors.NotFound:
        return False

@app.get("/health/{container_name}")
def check_health(container_name: str):
    if check_container_status(container_name):
        return {"status": "normal"}
    else:
        raise HTTPException(status_code=500, detail="Container status is abnormal")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
