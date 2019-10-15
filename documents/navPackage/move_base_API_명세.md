# dwa_local_planner::DWAPlanner Class Reference

[readme로 돌아가기](readme.md)

## Public Member Functions
bool __checkTrajectory__ (const Eigen::Vector3f pos, const Eigen::Vector3f vel, const Eigen::Vector3f vel_samples)


    Check if a trajectory is legal for a position/velocity pair . 
|   Parameters	 |   description	| data type|
|:---------------|---------------:  |---------:|
| pos            |the robot's pos   |Vector3f  |
|vel             |the robot's vel   |Vector3f  |
|vel_samples   	 |desired velocity  |Vector3f  |

>Returns True if the trajectory is valid, false otherwise => 자취가 유효한지 확인

 
bool __DWAPlanner__ (std::string name, base_local_planner::LocalPlannerUtil *planner_util)
 	
     Constructor for the planner. More...
|   Parameters	    |   description	    | data type     |
|:---------------   |---------------:   |---------:     |
|name               |planner's name     |string         |
|constmap_ros       |pointer            |Vector3f       |
|vel_samples   	    |desired velocity   |Vector3f       |


base_local_planner::Trajectory 	__findBestPath__ (const geometry_msgs::PoseStamped &global_pose, const geometry_msgs::PoseStamped &global_vel, geometry_msgs::PoseStamped &drive_velocities)
 	Given the current position and velocity of the robot, find the best trajectory to exectue. More...
    최적의 자취를 반환
 
bool 	__getCellCosts__ (int cx, int cy, float &path_cost, float &goal_cost, float &occ_cost, float &total_cost)
 	Compute the components and total cost for a map grid cell. More...
    cost 계산해주는거, path_cost 데이터에 자취에 대한 cost 계산, goal_cost 데이터는 goal 의 cost, occ_cost 는 occupancy grid 의 cost 계산 , total_cost 는 전체 cost 총합
 
double 	__getSimPeriod__ ()
 	Get the period at which the local planner is expected to run. More...
 
void 	__reconfigure__ (DWAPlannerConfig &cfg)
 	Reconfigures the trajectory planner. More...
 
bool 	__setPlan__ (const std::vector< geometry_msgs::PoseStamped > &orig_global_plan)
 
void 	__updatePlanAndLocalCosts__ (const geometry_msgs::PoseStamped &global_pose, const std::vector< geometry_msgs::PoseStamped > &new_plan, const std::vector< geometry_msgs::Point > &footprint_spec)
 	Update the cost functions before planning. More...
