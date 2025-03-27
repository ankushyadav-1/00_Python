import json

yt = 'youtube.text'

def load_data():
    try:
        with open( yt , 'r') as file:
            test = json.load(file)
            #print(type(test))
            return test
        
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(yt, 'w') as file:
        json.dump(videos, file)
        
def vid_list(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

def list_all_videos(videos):
    print('\n')
    print('*'*125)    
    vid_list(videos)
    print('\n')
    print('*'*125) 

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("Video added successfully")
    vid_list(videos)

def update_video(videos):
    list_all_videos(videos)        
    index = int(input("Enter video index: "))
    
    if 1<=index<=len(videos):
        name = input("Enter new video name: ")
        time = input("Enter video new duration: ")
        videos[index-1] = {"name": name, "time": time}
        save_data_helper(videos)
        
    else:
        print("Invalid index selected")
        
    print("Video updated successfully")
    vid_list(videos)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video index to delete: "))
    
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        
    else:
        print("Invalid video index selected")
        
    print("Video deleted successfully")
    vid_list(videos)

def main():
    videos = load_data()
    
    while True:
        print("\n YouTube Manager")
        print("1. list all YouTube videos")
        print("2. add a youtube video")
        print("3. update a youtube video details")
        print("4. delete a youtube video")
        print("5. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__": 
    main() 