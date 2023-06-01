import tkinter as tk

def main():
    def findGrade():
        def destroyOutput():
            output.destroy()
        c = float(current_grade.get()) / 100
        f = float(final_percent.get()) / 100
        g = float(grade.get()) / 100
        addedPercent = g - (1 - f) * c
        output=tk.Tk()
        output.title("Result")
        l=tk.Label(output,text="You need a " + str(round((addedPercent/f)*100,1)) + "% on the final to get a " + str(g*100)+"% in the class")
        l.pack()
        close=tk.Button(output,text="Close",command=destroyOutput)
        close.pack()
        output.mainloop()

    ui = tk.Tk()
    ui.title("Final Grade Calculator")
    l1 = tk.Label(ui, text="What grade do you have right now?")
    l1.pack()
    current_grade = tk.Entry(ui)
    current_grade.pack()
    l2 = tk.Label(ui, text="What percent of your grade is the final?")
    l2.pack()
    final_percent = tk.Entry(ui)
    final_percent.pack()
    l3 = tk.Label(ui, text="What is your desired final grade?")
    l3.pack()
    grade = tk.Entry(ui)
    grade.pack()
    b = tk.Button(ui, text="Enter", command=findGrade)
    b.pack(side="bottom")
    ui.mainloop()

if __name__ == "__main__":
    main()
