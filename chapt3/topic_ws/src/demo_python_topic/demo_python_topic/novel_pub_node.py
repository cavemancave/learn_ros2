import rclpy
from rclpy.node import Node 
import requests
from example_interfaces.msg import String
from queue import Queue

class NovelPubNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f'Node {node_name} has been started.')
        self.novel_queue_ = Queue()
        self.novel_publisher_ = self.create_publisher(String, 'novel', 10)
        self.create_timer(5, self.timer_callback)

    
    def timer_callback(self):
        if self.novel_queue_.empty():
            self.get_logger().info("No novel to publish.")
            return
        msg = String()
        msg.data = self.novel_queue_.get()
        self.get_logger().info(f"Publishing novel line: {msg.data}")
        self.novel_publisher_.publish(msg)

    def download(self, url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        for line in text.splitlines():
            self.novel_queue_.put(line)
        self.get_logger().info(f"Downloaded {url}: {len(text)} characters.")
        

def main():
    rclpy.init()
    node = NovelPubNode('novel_pub_node')
    node.download('http://0.0.0.0:8080/novel1.txt')
    node.download('http://0.0.0.0:8080/novel2.txt')
    node.download('http://0.0.0.0:8080/novel3.txt')
    rclpy.spin(node)
    rclpy.shutdown()