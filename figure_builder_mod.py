import matplotlib.pyplot as plt
import pandas as pd

class DataDisplay:
    def bar_chart(data, labels, title, filename):
        plt.figure(figsize=(8, 6))
        plt.bar(labels, data, color='skyblue')
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.title(title)
        plt.savefig(filename)
        plt.close()
    
    def line_chart(data, labels, title, filename):
        plt.figure(figsize=(8, 6))
        plt.plot(labels, data, marker='o', linestyle='-', color='red')
        plt.xlabel("Time")
        plt.ylabel("Values")
        plt.title(title)
        plt.grid()
        plt.savefig(filename)
        plt.close()
    
    def pie_chart(data, labels, title, filename):
        plt.figure(figsize=(8, 6))
        plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140, colors=['blue', 'red', 'green', 'orange'])
        plt.title(title)
        plt.savefig(filename)
        plt.close()
    
    def table_display(data, columns, filename):
        df = pd.DataFrame(data, columns=columns)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.auto_set_column_width([0, 1, 2])
        plt.savefig(filename)
        plt.close()
