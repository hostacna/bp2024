import rospy
from hexa_package.msg import JointState

def joint_state_callback(msg):
    # Process the received JointState message
    print("Received Joint State Message:")
    print("Names:", msg.name)
    print("Positions:", msg.position)

def subscribe_to_joint_states():
    rospy.init_node('listener')
    rospy.Subscriber('/joint_states', JointState, joint_state_callback)
    rospy.spin()

if __name__ == '__main__':
    subscribe_to_joint_states()