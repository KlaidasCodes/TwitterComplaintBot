from classes import *

# consts ##############
USERNAME = "asilenas69"
PASSWORD = "klaidas12"
MIN_DOWN_SPEED = 50
MIN_UP_SPEED = 20
# consts #############

robot = InternetSpeedTwitterBot(username=USERNAME, password=PASSWORD, min_down_speed=MIN_DOWN_SPEED,
                                min_up_speed=MIN_UP_SPEED)
robot.get_internet_speed()
if robot.down_speed < MIN_DOWN_SPEED or robot.upload_speed < MIN_UP_SPEED:
    time.sleep(uniform(5.0, 7.0))
    robot.tweet_at_provider()

