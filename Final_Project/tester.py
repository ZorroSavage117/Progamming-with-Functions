import saving
import datetime

data = saving.session_start()
currenttime = datetime.date.today().strftime("%Y-%m-%d")

print(f"dist: {data}")
roll_list = [1, 3, 2, 4]
saving.session_storage_update(data[currenttime], roll_list, 4)
roll_list = [1, 3, 2, 4]
saving.session_storage_update(data[currenttime], roll_list, 4)
roll_list = [1, 3, 2, 4]
saving.session_storage_update(data[currenttime], roll_list, 4)

saving.session_save(data)

saves = saving.load_saves()
print(f"saves: {saves}")