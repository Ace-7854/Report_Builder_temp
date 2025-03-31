from pdf_builder_mod import PDFReport as pd_rep
from datetime import datetime

def get_sanitized_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def generate_report(title, figure, caption):
    report = pd_rep(title, "CiB Week Overview")
    report.add_title_page()
    report.add_summary("This is a placeholder for the summary of your report. You can dynamically add project insights here.")
    table_data = [["Data1", "Data2", "Data3"], ["Value1", "Value2", "Value3"], ["Entry1", "Entry2", "Entry3"]]
    #report.add_table(table_data)
    report.add_figure(f"sample_product/{figure}", caption=caption)
    report.save_pdf(f"reports/{title}{get_sanitized_timestamp()}.pdf")

def make_figure():
    from figure_builder_mod import DataDisplay
    data = [22, 51, 23, 100]
    labels = ["A", "B", "C", "D"]
    DataDisplay.bar_chart(data, labels, "Sample Bar Chart", "sample_product/barchart.png")
    DataDisplay.line_chart(data, labels, "Sample Line Chart", "sample_product/linechart.png")
    DataDisplay.pie_chart(data, labels, "Sample Pie Chart", "sample_product/piechart.png")
    DataDisplay.table_display([["Sunday", 2, 456, 22], ["Monday", 5, 6,20], ["Tuesday", 8, 9,10]], ["Day", "Number of deaths", "Number of Craniums", "Number of pies"], "sample_product/table.png")


def main():
    generate_report("CiB Project", "table.png", "This is my table")
    make_figure()

if __name__ == "__main__":
    main()