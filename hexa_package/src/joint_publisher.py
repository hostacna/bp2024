import rospy
from hexa_package.msg import JointState

def publish_joint_state():
    rospy.init_node('joint_state_publisher')
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # Create a JointState message
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = ['joint1', 'joint2', 'joint3']
        joint_state_msg.position = [1.2, -0.5, 0.8]

        # Publish the message
        pub.publish(joint_state_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_state()
    except rospy.ROSInterruptException:
        pass