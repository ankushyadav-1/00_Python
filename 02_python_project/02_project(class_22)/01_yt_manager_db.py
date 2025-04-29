import sqlite3

conn = sqlite3.connect('yt_videos.db')

cursor = conn.cursor()


cursor.execute(''' 
    create table if not exists videos (
        id integer primary key ,
        name text not null,
        time text not null
        )          
        ''')

def list_videos():
    cursor.execute('select * from videos')
    for row in cursor.fetchall():
        print(row)
        

def add_video(name, time):  
    cursor.execute('insert into videos (name, time) values (?, ?)', (name, time))
    conn.commit()


def update_video(video_id, new_name, new_time):
    cursor.execute('update videos set name = ?, time = ? where id = ?', (new_name, new_time, video_id))
    conn.commit()
    

def delete_video(video_id):
    cursor.execute('delete from videos where id = ?', (video_id,))
    conn.commit()
    

def main():
    while True:
        print("\n YouTube Manager")
        print("1. list all YouTube videos")
        print("2. add a youtube video")
        print("3. update a youtube video details")
        print("4. delete a youtube video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
            
            
        elif choice == "2":
            list_videos()
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
            
            
        elif choice == "3":
            list_videos()
            vid_id = input("Enter video id to update: ")
            name = input("Enter new video name: ")
            time = input("Enter video duration: ")
            update_video(vid_id, name, time)

        elif choice == "4":
            list_videos()
            vid_id = input("Enter video id to delete: ")
            delete_video(vid_id)
            
        elif choice == "5":
            break
        
        else:
            print("Invalid choice")

    conn.close()

if __name__ == '__main__':
    main()