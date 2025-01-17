import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
import traceback
import time
from threading import Thread
from django.utils import timezone
import pytz

class EmailService:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = "hethongduadonhocsinh@gmail.com"
        self.password = "crkx yhbf lbtj yzua"
        self.max_retries = 3
        self.retry_delay = 2  # seconds
        self.vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
        
        # Danh sách email nhận cảnh báo
        self.admin_emails = [
            'ntcaophi2009@gmail.com',  # Email chính
            # 'quanly@gmail.com',                 # Email quản lý
            # 'hieutruong@gmail.com',             # Email hiệu trưởng
            # # Thêm các email khác nếu cần
        ]

    def format_vietnam_time(self, current_time):
        vietnam_time = current_time.astimezone(self.vietnam_tz)
        return vietnam_time.strftime('%H:%M:%S %d/%m/%Y')

    def send_email_async(self, student, bus, action, current_time):
        """Send email in a separate thread"""
        thread = Thread(
            target=self.send_bus_notification,
            args=(student, bus, action, current_time)
        )
        thread.start()

    def send_bus_notification(self, student, bus, action, current_time):
        if not student.email:
            print(f"No email address for student {student.name}")
            return False

        for attempt in range(self.max_retries):
            try:
                print(f"\nAttempt {attempt + 1} to send email for {student.name}")
                print(f"Email: {student.email}")
                print(f"Action: {action}")

                # Create message container
                msg = MIMEMultipart('alternative')
                msg['Subject'] = f'Thông báo xe bus - {student.name}'
                msg['From'] = self.sender_email
                msg['To'] = student.email

                # Format time in Vietnam timezone
                vietnam_time = self.format_vietnam_time(current_time)

                # Create the context for the email template
                context = {
                    'student_name': student.name,
                    'bus_name': bus.name,
                    'bus_route': bus.route,
                    'driver_name': bus.driver_name,
                    'driver_phone': bus.driver_phone,
                    'action': 'lên xe' if action == 'check_in' else 'xuống xe',
                    'time': vietnam_time
                }

                # Create HTML content
                html_content = render_to_string('email/bus_notification.html', context)
                html_part = MIMEText(html_content, 'html', 'utf-8')
                msg.attach(html_part)

                # Connect to SMTP server with explicit SSL/TLS
                with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
                    server.set_debuglevel(1)  # Enable debug output
                    server.starttls()
                    print("Logging in to SMTP server...")
                    server.login(self.sender_email, self.password)
                    print("Sending email...")
                    server.send_message(msg)
                    print(f"Email sent successfully to {student.email}")
                    return True

            except Exception as e:
                print(f"\nError on attempt {attempt + 1}:")
                print(f"Error type: {type(e).__name__}")
                print(f"Error message: {str(e)}")
                print("Traceback:")
                print(traceback.format_exc())
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                return False

        return False

    def send_students_on_bus_warning(self, bus, students):
        """Send warning email when bus is offline with students onboard"""
        for attempt in range(self.max_retries):
            try:
                print(f"\nAttempt {attempt + 1} to send warning email for bus {bus.name}")

                # Create message container
                msg = MIMEMultipart('alternative')
                msg['Subject'] = f'CẢNH BÁO KHẨN CẤP: Còn học sinh trên xe {bus.name} khi xe ngừng hoạt động'
                msg['From'] = self.sender_email
                msg['To'] = ', '.join(self.admin_emails)  # Gửi đến tất cả email trong danh sách

                # Format current time in Vietnam timezone
                current_time = timezone.now()
                vietnam_time = self.format_vietnam_time(current_time)

                # Create the context for the email template
                context = {
                    'bus_name': bus.name,
                    'bus_route': bus.route,
                    'driver_name': bus.driver_name,
                    'driver_phone': bus.driver_phone,
                    'students': students,
                    'time': vietnam_time
                }

                # Create HTML content
                html_content = render_to_string('email/students_on_bus_warning.html', context)
                html_part = MIMEText(html_content, 'html', 'utf-8')
                msg.attach(html_part)

                # Connect to SMTP server with explicit SSL/TLS
                with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
                    server.set_debuglevel(1)  # Enable debug output
                    server.starttls()
                    print("Logging in to SMTP server...")
                    server.login(self.sender_email, self.password)
                    print("Sending warning email...")
                    # Gửi email đến tất cả địa chỉ trong admin_emails
                    server.send_message(msg)
                    print(f"Warning email sent successfully to {self.admin_emails}")
                    return True

            except Exception as e:
                print(f"\nError on attempt {attempt + 1}:")
                print(f"Error type: {type(e).__name__}")
                print(f"Error message: {str(e)}")
                print("Traceback:")
                print(traceback.format_exc())
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                return False

        return False 