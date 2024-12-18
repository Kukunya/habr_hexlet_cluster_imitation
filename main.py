from app.cluster.buffer import Buffer
from app.cluster.cluster import Cluster
from app.interface.cli import Cli

if __name__ == "__main__":
    buffer = Buffer()  # Shared task buffer
    while True:
        server_count = input("Specify the number of servers: ")  # Number of servers
        if server_count.isdigit():
            server_count = int(server_count)
            break
        print("A number must be specified")

    cluster = Cluster(buffer, server_count)  # Initialize the cluster

    # Start server threads
    cluster.start()

    # CLI runs in the main thread
    cli = Cli(cluster, buffer)
    try:
        cli.run()
    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("\nExiting program.")
    finally:
        # Ensure all servers are stopped
        cluster.stop()
