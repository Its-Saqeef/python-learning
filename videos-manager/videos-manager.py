import sqlite3

conn = sqlite3.connect("videos-manager.db")
cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                duration TEXT NOT NULL
                )
    ''')

def load_videos():
    res = cur.execute("Select * from videos")
    return res.fetchall()

def list_all_videos(videos):
    for video in videos:
        print(video)
   
    
def add_video(name,time):
    cur.execute("""
    INSERT INTO VIDEOS(title,duration) values(?,?)
    """,(name,time))
    conn.commit()
    print("Video added successfully")

def update_video(id,name,duration):
    cur.execute('''
        update videos
        set title = ? , duration = ?
        where id = ?
''',(name,duration,id))
    conn.commit()
    print("Video updated successfully")

def delete_video(id):
    cur.execute("Delete from videos where id = ?",(id,))
    conn.commit()
    print("Video deleted successfully")


videos =load_videos()

def main():
    while True:
        print("\n")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        
        choice = input("Enter your choice : ")

        match choice:
            case "1":
                list_all_videos(videos)
                for i in range(1,40):
                    print("*", end="")
            
            case "2":
                title = input("Enter title of the video : ")
                duration = input("Enter duration of video : ")

                add_video(title,duration)
            case "3":
                id= input("Enter video id : ")
                title = input("Enter new title : ")
                duration = input("Enter new duration : ")

                update_video(id,title,duration)
            case "4":
                id= input("Enter video id : ")

                delete_video(id)
            case "5":
                break

            case _:
                print("Invalid Choice")
            
    conn.close()


if __name__ == "__main__":
    main()