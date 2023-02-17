import json
import pygame # just for graphics to visualize the robot arm without the need of a real robot arm
import numpy as np 
#just testing out some ideas for the robot arm and angle calculations which will later be written in c++

attachment_length=0 #no attachment

# new class segment 
class segment ():

    def __init__(self, name, length, rotation, rMin,rMax,pointing_direction=[0,0,1]):
        self.name=name
        self.length=length
        self.rotation=rotation
        self.rtrange=[rMin,rMax]
        self.currentangle=0
        self.rotationspeed=1 # rotation speed in degrees per second
        self.start_point=[0,0,0]
        self.end_point=[0,0,0]
        self.pointing_direction=pointing_direction

class arm ():
    def __init__(self, segments):
        self.segments=segments
        self.postion=(0,0,0)    #position of the endpiece
        self.direction=(0,0,1)  #direction of the endpiece

segments=[
    segment("A", 10, [0,0,1], 0,360), #rotatin along the z axis
    segment("B", 35, [1,0,0], 0,360), #rotatin along the x axis
    segment("C", 30, [1,0,0], 0,360), #rotatin along the x axis
    segment("D", 20, [1,0,0], 0,360), #rotatin along the x axis
    segment("E", 10, [0,0,1], 0,360), #rotatin along the z axis endpiece
    segment("F", 10+attachment_length, (0,1,0), 0,360), #rotatin along the y axis endpiece
]

#reading the current angle of the segment from json file and setting it to the current angle
data = json.load(open("log.json"))
for i in range(len(segments)):
    print(segments[i].name) 
    #reading the current angle of the segment from json file and setting it to the current angle
    try:
        segments[i].currentangle= json.load(open("log.json"))[segments[i].name]
    except:
        segments[i].currentangle=180
        #reading all data from json an saving it to the variable data
        
        data[segments[i].name]=segments[i].currentangle
  
    #print the current angle of the segment
    print(str(segments[i].currentangle))

#writing data to json file 
with open('log.json', 'w') as outfile:
    json.dump(data, outfile)

# @Todo: calculate the current position of the endpiece and the direction of the endpiece^
def calc_positions(segments):
    #calculating the current position of the endpiece
    
    for i in range(len(segments)):
        if i==0:
            segment[i].start_point =[0,0,0]
        else:
            segment[i].start_point=segments[i-1].end_poinst

        absolute_vector=segment[i].rotation

        currentPosition=(currentPosition[0]+segments[i].length*np.sin(segments[i].currentangle), currentPosition[1]+segments[i].length*np.cos(segments[i].currentangle), currentPosition[2])
    return currentPosition

def get_end_position():
    return segment[segments.__len__()-1].end_point

def calc_direction(segments):
    #calculating the current direction of the endpiece
    currentDirection=[0,0,1]
    for i in range(len(segments)):
        currentDirection=(currentDirection[0]+segments[i].length*np.sin(segments[i].currentangle), currentDirection[1]+segments[i].length*np.cos(segments[i].currentangle), currentDirection[2])
    return currentDirection
#calculating the current position of the endpiece and the direction of the endpiece

currentPosition=get_end_position #current position of the endpiece
currentDirection=calc_direction(segments) #current direction of the endpiece

print ("current position: "+str(currentPosition)+"and current direction: "+str(currentDirection))


#calculating the new angle of the segment 

#figuring out hot to get to the ditance with the least movement / the fastetst way to get to the new position

#def mainloop():
    #all the robot calculations


#pygame stuff


#ask for the new postition and pointing direction of the endpiece
newposition=input("new position: ") #new position of the endpiece
newdirection=input("new direction: ") #new direction of the endpiece

SCREEN_W, SCREEN_H = 800, 600
FOV_V = np.pi/4 # 45 degrees vertical fov
FOV_H = FOV_V*SCREEN_W/SCREEN_H


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    running = True
    clock = pygame.time.Clock()
    surf = pygame.surface.Surface((SCREEN_W, SCREEN_H))

    points = np.asarray([[1, 1, 1, 1, 1], [4, 2, 0, 1, 1], [1, .5, 3, 1, 1]])

    # giving points to define the origin as well as the x, y and z axis
    origin_scale=5
    origin =np.array([0,0,0,1,1])
    x_axis =np.array([origin_scale,0,0,1,1])
    y_axis =np.array([0,origin_scale,0,1,1])
    z_axis =np.array([0,0,origin_scale,1,1])
    origin_points=[origin,x_axis,y_axis,z_axis]
    

    triangles = np.asarray([[0,1,2]])
    #points, triangles =  read_obj('obj models/teapot.obj')
    color_scale = 230/np.max(np.abs(points))

    camera = np.asarray([13, 0.5, 2, 3.3, 0])
    z_order = np.zeros(len(triangles))
    shade = z_order.copy()

    #pygame main loop in which the robot video simulation is running
    while running: 
        #pygame display setup
        pygame.mouse.set_pos(SCREEN_W/2, SCREEN_H/2)
        surf.fill([50,127,200])
        elapsed_time = clock.tick()*0.001
        light_dir = np.asarray([np.sin(pygame.time.get_ticks()/1000), 1, 1])
        light_dir = light_dir/np.linalg.norm(light_dir)
        #pygame quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: running = False
        # projecting the points sorting the triangles by z order and calculating the shade
        project_points(points, camera)
        sort_triangles(points, triangles, camera, light_dir, z_order, shade) 

        project_points(origin_points, camera)  

        #drawing the origin points  
        for i in origin_points:
            pygame.draw.circle(surf, (0,0,255), (int(i[3]), int(i[4])), 5)
        #drawing the orgin as wellas the main axis
        pygame.draw.line(surf, (20,20,20), (int(origin_points[0][3]), int(origin_points[0][4])), (int(origin_points[1][3]), int(origin_points[1][4])), 2)
        pygame.draw.line(surf, (20,20,20), (int(origin_points[0][3]), int(origin_points[0][4])), (int(origin_points[2][3]), int(origin_points[2][4])), 2)
        pygame.draw.line(surf, (20,20,20), (int(origin_points[0][3]), int(origin_points[0][4])), (int(origin_points[3][3]), int(origin_points[3][4])), 2)
        
        #drawing the triangles
        for index in np.argsort(z_order):
            if z_order[index] == 9999: break
            triangle = [points[triangles[index][0]][3:], points[triangles[index][1]][3:], points[triangles[index][2]][3:]]
            color = shade[index]*np.abs(points[triangles[index][0]][:3])*color_scale +25
            pygame.draw.polygon(surf, color, triangle)

        #mainloop()
        
        #Updating the display
        screen.blit(surf, (0,0)); pygame.display.update()
        pygame.display.set_caption(str(round(1/(elapsed_time+1e-16), 1)) + ' ' + str(camera))
        movement(camera, elapsed_time*10)
        

 #TODO: better vertical projection



 
def project_points(points, camera):

    for point in points:
        # Calculate xy angle of vector from camera point to projection point
        h_angle_camera_point = np.arctan((point[2]-camera[2])/(point[0]-camera[0] + 1e-16))
        
        # Check if it isn't pointing backwards
        if abs(camera[0]+np.cos(h_angle_camera_point)-point[0]) > abs(camera[0]-point[0]):
            h_angle_camera_point = (h_angle_camera_point - np.pi)%(2*np.pi)

        # Calculate difference between camera angle and pointing angle
        h_angle = (h_angle_camera_point-camera[3])%(2*np.pi)
        
        # Bring to -pi to pi range
        if h_angle > np.pi: h_angle =  h_angle - 2*np.pi
        
        # Calculate the point horizontal screen coordinate
        point[3] = SCREEN_W*h_angle/FOV_H + SCREEN_W/2

        # Calculate xy distance from camera point to projection point
        distance = np.sqrt((point[0]-camera[0])**2 + (point[1]-camera[1])**2 + (point[2]-camera[2])**2)
        
        # Calculate angle to xy plane
        v_angle_camera_point = np.arcsin((camera[1]-point[1])/distance)

        # Calculate difference between camera verticam angle and pointing vertical angle
        v_angle = (v_angle_camera_point - camera[4])%(2*np.pi)
        if v_angle > np.pi: v_angle =  v_angle - 2*np.pi

        # Bring to -pi to pi range
        if v_angle > np.pi: v_angle =  v_angle - 2*np.pi

        # Calculate the point vertical screen coordinate
        point[4] = SCREEN_H*v_angle/FOV_V + SCREEN_H/2


def dot_3d(arr1, arr2):
    return arr1[0]*arr2[0] + arr1[1]*arr2[1] + arr1[2]*arr2[2]

def sort_triangles(points, triangles, camera, light_dir, z_order, shade):
    for i in range(len(triangles)):
        triangle = triangles[i]

        # Use Cross-Product to get surface normal
        vet1 = points[triangle[1]][:3]  - points[triangle[0]][:3]
        vet2 = points[triangle[2]][:3] - points[triangle[0]][:3]

        # backface culling with dot product between normal and camera ray
        normal = np.cross(vet1, vet2)
        normal = normal/np.sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2])
        
        CameraRay = points[triangle[0]][:3] - camera[:3]
        dist2cam = np.sqrt(CameraRay[0]*CameraRay[0] + CameraRay[1]*CameraRay[1] + CameraRay[2]*CameraRay[2])
        CameraRay = CameraRay/dist2cam

        # get projected 2d points for filtering of offscreen triangles
        xxs = np.asarray([points[triangle[0]][3:5][0],  points[triangle[1]][3:5][0],  points[triangle[2]][3:5][0]])
        yys = np.asarray([points[triangle[0]][3:5][1],  points[triangle[1]][3:5][1],  points[triangle[2]][3:5][1]])

        # check valid values
        if (dot_3d(normal, CameraRay) < 0   and np.min(xxs) > - SCREEN_W and np.max(xxs) < 2*SCREEN_W
                                            and np.min(yys) > - SCREEN_H and np.max(yys) < 2*SCREEN_H):
            
            z_order[i] = -dist2cam

            # calculate shading, normalize, dot and to 0 - 1 range
            shade[i] = 0.5*dot_3d(light_dir, normal) + 0.5

        # big value for last positions in sort
        else: z_order[i] = 9999

def movement(camera, elapsed_time):

    if pygame.mouse.get_focused():
        p_mouse = pygame.mouse.get_pos()
        camera[3] = (camera[3] + 10*elapsed_time*np.clip((p_mouse[0]-SCREEN_W/2)/SCREEN_W, -0.2, .2))%(2*np.pi)
        camera[4] = camera[4] + 10*elapsed_time*np.clip((p_mouse[1]-SCREEN_H/2)/SCREEN_H, -0.2, .2)
        camera[4] = np.clip(camera[4], -.3, .3)
    
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[ord('e')]: camera[1] += elapsed_time
    elif pressed_keys[ord('q')]: camera[1] -= elapsed_time

    if (pressed_keys[ord('w')] or pressed_keys[ord('s')]) and (pressed_keys[ord('a')] or pressed_keys[ord('d')]):
        elapsed_time *= 0.707 # keep speed for diagonals
        
    if pressed_keys[pygame.K_UP] or pressed_keys[ord('w')]:
        camera[0] += elapsed_time*np.cos(camera[3])
        camera[2] += elapsed_time*np.sin(camera[3])

    elif pressed_keys[pygame.K_DOWN] or pressed_keys[ord('s')]:
        camera[0] -= elapsed_time*np.cos(camera[3])
        camera[2] -= elapsed_time*np.sin(camera[3])
        
    if pressed_keys[pygame.K_LEFT] or pressed_keys[ord('a')]:
        camera[0] += elapsed_time*np.sin(camera[3])
        camera[2] -= elapsed_time*np.cos(camera[3])
        
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[ord('d')]:
        camera[0] -= elapsed_time*np.sin(camera[3])
        camera[2] += elapsed_time*np.cos(camera[3])

def read_obj(fileName):
    vertices = []
    triangles = []
    f = open(fileName)
    for line in f:
        if line[:2] == "v ":
            index1 = line.find(" ") + 1
            index2 = line.find(" ", index1 + 1)
            index3 = line.find(" ", index2 + 1)
            
            vertex = [float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1]), 1, 1]
            vertices.append(vertex)

        elif line[0] == "f":
            index1 = line.find(" ") + 1
            index2 = line.find(" ", index1 + 1)
            index3 = line.find(" ", index2 + 1)

            triangles.append([int(line[index1:index2]) - 1, int(line[index2:index3]) - 1, int(line[index3:-1]) - 1])

    f.close()

    return np.asarray(vertices), np.asarray(triangles)


if __name__ == '__main__':
    main()
    pygame.quit()

# all possible ways to reach a certain point are beeing calculated and returned as a ranges of angles for each joint then the joint, which would take longest to react the closest border its rannge determines which of the possible combinations of angels is used