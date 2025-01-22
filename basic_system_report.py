import psutil
import matplotlib.pyplot as plt
from datetime import datetime
from fpdf import FPDF

# Get basic system data
def get_system_data():
    return {
        'mem': psutil.virtual_memory(),
        'disk': psutil.disk_usage('/'),
        'users_count': len(psutil.users()),
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# Create simple charts
def create_charts(data):
    # Memory chart
    plt.figure(figsize=(4, 4))
    plt.pie([data['mem'].used, data['mem'].available], 
            labels=['Used', 'Free'], 
            autopct='%1.1f%%', colors=['#FF9999', '#99FF99'])
    plt.title('Memory Usage')
    mem_chart = 'memory_chart.png'
    plt.savefig(mem_chart)
    plt.close()

    # Disk chart
    plt.figure(figsize=(4, 4))
    plt.pie([data['disk'].used, data['disk'].free], 
            labels=['Used', 'Free'], 
            autopct='%1.1f%%', colors=['#99CCFF', '#FFCC99'])
    plt.title('Disk Usage')
    disk_chart = 'disk_chart.png'
    plt.savefig(disk_chart)
    plt.close()

    return mem_chart, disk_chart

# Generate a simple PDF report
def generate_pdf(data, mem_chart, disk_chart):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Title
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Basic System Report", ln=True, align="C")
    pdf.ln(8)

    # Basic information
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, txt=f"Report Time: {data['time']}", ln=True)
    pdf.cell(0, 10, txt=f"Connected Users: {data['users_count']}", ln=True)

    # Memory usage
    pdf.ln(5)
    pdf.cell(0, 10, txt="Memory Usage:", ln=True)
    pdf.image(mem_chart, x=10, y=pdf.get_y(), w=80)
    pdf.ln(50)

    # Disk usage
    pdf.cell(0, 10, txt="Disk Usage:", ln=True)
    pdf.image(disk_chart, x=10, y=pdf.get_y(), w=80)

    # Save PDF
    pdf_file = "basic_report.pdf"
    pdf.output(pdf_file)
    print(f"PDF report generated: {pdf_file}")

if __name__ == "__main__":
    system_data = get_system_data()
    memory_chart, disk_chart = create_charts(system_data)
    generate_pdf(system_data, memory_chart, disk_chart)
