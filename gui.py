import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def bmiCal(Weight, Height):
    bmi = (Weight / (Height ** 2)) * 703
    return bmi

def calculate_bmi():
    name = name_entry.get()
    age = int(age_entry.get())
    Gender = gender_var.get()
    Height = float(height_entry.get())
    Weight = float(weight_entry.get())

    bmi = bmiCal(Weight, Height)

    if age >= 0 and age < 2:
        mini_cal = 800
    elif age >= 2 and age < 4:
        mini_cal = 1400
    elif age >= 4 and age < 8:
        mini_cal = 1800
    else:
        mini_cal = 0

    bmi_label.config(text="BMI: {:.2f}".format(bmi))

    if bmi < 16:
        result_label.config(text="Severely Underweight")
    elif 16 <= bmi < 18.5:
        result_label.config(text="Underweight")
    elif 18.5 <= bmi < 25:
        result_label.config(text="Healthy")
    elif 25 <= bmi < 30:
        result_label.config(text="Overweight")
    elif bmi >= 30:
        result_label.config(text="Obese")

def record_data():
    with open("records.txt", "a") as file:
        file.write("\n" + name_entry.get() + "\n" + age_entry.get() + "\n" + gender_var.get() + "\n" + str(daily_intake_in_cal) + "\n" + bmi_label.cget("text"))

def record_calories():
    global daily_intake_in_cal
    daily_intake_in_cal = 0

    for i in range(len(food)):
        quantity = float(food_entries[i].get())
        daily_intake_in_cal += (quantity / 100) * calval[i]

    calories_label.config(text="Daily calorie Consumption: {:.2f} Calories".format(daily_intake_in_cal))

    record_data()
    messagebox.showinfo("Recorded", "Data has been recorded successfully!")

root = tk.Tk()
root.geometry("400x600")
root.title("Nutrition Calculator")
root.config(background="#0191b9")



background_image = Image.open("C:\\Users\\ayush\\OneDrive\\Desktop\\Python Project\\GUI\\we2.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)
background_label.image = background_photo 

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Enter your age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

gender_label = tk.Label(root, text="M/F:")
gender_label.pack()
gender_var = tk.StringVar(value="M")
gender_entry = tk.Entry(root, textvariable=gender_var)
gender_entry.pack()

height_label = tk.Label(root, text="Enter your height (in inches):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="Enter your Weight (in pounds):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

bmi_label = tk.Label(root, text="BMI: ")
bmi_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()


food = ["milk", "egg", "rice", "lentils", "vegetables", "Meat"]
calval = [100, 150, 130, 113, 185, 143]
food_entries = []

for i in range(len(food)):
    food_label = tk.Label(root, text=f"{food[i]} (in grams):")
    food_label.pack()
    food_entry = tk.Entry(root)
    food_entry.pack()
    food_entries.append(food_entry)

calculate_calories_button = tk.Button(root, text="Calculate Calories", command=record_calories)
calculate_calories_button.pack()

calories_label = tk.Label(root, text="Daily calorie Consumption:")
calories_label.pack()

root.mainloop()
