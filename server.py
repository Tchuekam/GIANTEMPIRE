import http.server
import json
import os
import re
import urllib.parse
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

# Enterprise HTML Email Template with JSON-LD Event Reservation Markup
EMAIL_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Confirmed: GianTecH Empire Consultation</title>
  
  <!-- JSON-LD Event Reservation Schema for Gmail & Outlook automated inbox actions -->
  <script type="application/ld+json">
  {{
    "@context": "http://schema.org",
    "@type": "EventReservation",
    "reservationNumber": "GT-{reservation_id}",
    "reservationStatus": "http://schema.org/Confirmed",
    "underName": {{
      "@type": "Person",
      "name": "{name}"
    }},
    "reservationFor": {{
      "@type": "Event",
      "name": "GianTecH Consultation: {product}",
      "startDate": "{iso_start}",
      "endDate": "{iso_end}",
      "location": {{
        "@type": "VirtualLocation",
        "name": "Google Meet",
        "url": "{meeting_url}"
      }}
    }}
  }}
  </script>
  
  <style>
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background-color: #08090a;
      color: #d1d2d5;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}
    .email-container {{
      max-width: 600px;
      margin: 40px auto;
      background-color: #0f1011;
      border: 1px solid #1f2023;
      border-top: 4px solid #00F2FE;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    }}
    .header {{
      padding: 30px 40px 20px 40px;
      text-align: center;
      border-bottom: 1px solid #1f2023;
    }}
    .logo {{
      height: 34px;
      vertical-align: middle;
    }}
    .content {{
      padding: 40px;
    }}
    .tag {{
      display: inline-block;
      background: rgba(0, 242, 254, 0.1);
      color: #00F2FE;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      padding: 6px 12px;
      border-radius: 20px;
      margin-bottom: 20px;
    }}
    h1 {{
      color: #ffffff;
      font-size: 24px;
      font-weight: 700;
      margin-top: 0;
      margin-bottom: 16px;
      letter-spacing: -0.5px;
    }}
    p {{
      font-size: 15px;
      line-height: 1.6;
      color: #8f9095;
      margin-top: 0;
      margin-bottom: 24px;
    }}
    .details-box {{
      background-color: #151618;
      border: 1px solid #252629;
      border-radius: 10px;
      padding: 24px;
      margin-bottom: 30px;
    }}
    .details-grid {{
      width: 100%;
      border-collapse: collapse;
    }}
    .details-grid td {{
      padding: 10px 0;
      border-bottom: 1px solid #252629;
      font-size: 14px;
    }}
    .details-grid tr:last-child td {{
      border-bottom: none;
      padding-bottom: 0;
    }}
    .details-grid tr:first-child td {{
      padding-top: 0;
    }}
    .details-label {{
      width: 120px;
      color: #606165;
      font-weight: 600;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.8px;
    }}
    .details-value {{
      color: #ffffff;
    }}
    .btn-container {{
      margin: 30px 0;
      display: flex;
    }}
    .btn {{
      display: inline-block;
      background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%);
      color: #08090a !important;
      text-decoration: none;
      padding: 14px 30px;
      font-size: 14px;
      font-weight: 600;
      border-radius: 30px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0, 242, 254, 0.35);
      transition: all 0.3s ease;
      margin-right: 12px;
    }}
    .btn-secondary {{
      background: #1f2023;
      border: 1px solid #35363a;
      color: #ffffff !important;
      box-shadow: none;
    }}
    .section-title {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-top: 30px;
      margin-bottom: 12px;
    }}
    .checklist-item {{
      display: flex;
      margin-bottom: 10px;
      font-size: 13.5px;
      color: #8f9095;
      line-height: 1.5;
    }}
    .checklist-icon {{
      color: #00F2FE;
      margin-right: 10px;
      font-weight: bold;
    }}
    .footer {{
      background-color: #0c0d0e;
      padding: 35px 40px;
      text-align: center;
      border-top: 1px solid #1f2023;
      font-size: 11.5px;
      color: #606165;
      line-height: 1.8;
    }}
    .footer a {{
      color: #00F2FE;
      text-decoration: none;
    }}
    .disclaimer {{
      margin-top: 20px;
      font-size: 10px;
      color: #45464a;
      text-align: justify;
    }}
    .divider {{
      height: 1px;
      background-color: #1f2023;
      margin: 30px 0;
    }}
  </style>
</head>
<body>
  <div class="email-container">
    <div class="header">
      <img src="https://giantech.app/giantech_files/logo.png" alt="GianTecH Logo" class="logo" onerror="this.src='https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/644918964e907d2eeb9e57cb_Logo.png';">
    </div>
    <div class="content">
      <div class="tag">Confirmed</div>
      <h1>Consultation Scheduled</h1>
      <p>Dear {name},</p>
      <p>We are pleased to confirm your upcoming consultation with GianTecH Empire. Our technical architects will walk you through the product integration strategy and explore automations tailored to your workflow.</p>
      
      <div class="details-box">
        <table class="details-grid">
          <tr>
            <td class="details-label">Date</td>
            <td class="details-value">{date}</td>
          </tr>
          <tr>
            <td class="details-label">Time</td>
            <td class="details-value">{time} (45 mins)</td>
          </tr>
          <tr>
            <td class="details-label">Solution</td>
            <td class="details-value">{product}</td>
          </tr>
          <tr>
            <td class="details-label">Video Link</td>
            <td class="details-value"><a href="{meeting_url}" style="color: #00F2FE; text-decoration: none; font-weight: 600;">{meeting_url}</a></td>
          </tr>
          <tr>
            <td class="details-label">Ref ID</td>
            <td class="details-value" style="font-family: monospace;">GT-{reservation_id}</td>
          </tr>
        </table>
      </div>

      <div class="btn-container">
        <a href="{meeting_url}" class="btn">Join Video Call</a>
        <a href="{calendar_url}" target="_blank" class="btn btn-secondary">Add to Calendar</a>
      </div>

      <div class="divider"></div>
      
      <div class="section-title">Pre-Session Checklist</div>
      <div class="checklist-item">
        <span class="checklist-icon">✓</span>
        <span>Please check your camera and microphone setup on Google Meet before the meeting.</span>
      </div>
      <div class="checklist-item">
        <span class="checklist-icon">✓</span>
        <span>Have details about your current system stack and manual workflows ready.</span>
      </div>
      <div class="checklist-item">
        <span class="checklist-icon">✓</span>
        <span>Feel free to invite other stakeholders to join the call via the meeting link.</span>
      </div>

      {notes_section}
      
    </div>
    <div class="footer">
      <p>GianTecH Empire LLC &bull; 100 Innovation Way &bull; Tech District &bull; Silicon Valley & Douala</p>
      <p>To reschedule your briefing, please visit our <a href="#">Client Portal</a> or contact support@giantech.app.</p>
      <p>&copy; {current_year} GianTecH Empire. All rights reserved.</p>
      
      <div class="disclaimer">
        CONFIDENTIALITY NOTICE: This transmission is intended only for the use of the individual or entity named above and contains information that is confidential. If you are not the intended recipient, please destroy all copies and notify the sender immediately.
      </div>
    </div>
  </div>
</body>
</html>
"""

# Host notification template
HOST_EMAIL_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>New Booking: GianTecH Empire</title>
  <style>
    body {{
      font-family: sans-serif;
      background-color: #08090a;
      color: #d1d2d5;
      padding: 30px;
    }}
    .container {{
      max-width: 600px;
      margin: 0 auto;
      background-color: #0f1011;
      border: 1px solid #1f2023;
      border-top: 4px solid #00F2FE;
      border-radius: 8px;
      padding: 30px;
    }}
    h1 {{
      color: #fff;
      font-size: 20px;
      margin-top: 0;
    }}
    table {{
      width: 100%;
      margin: 20px 0;
    }}
    td {{
      padding: 8px 0;
      border-bottom: 1px solid #252629;
    }}
    .label {{
      color: #606165;
      font-weight: bold;
      width: 120px;
    }}
    .val {{
      color: #fff;
    }}
    .notes-box {{
      background: #151618;
      border: 1px solid #252629;
      padding: 15px;
      border-radius: 4px;
      font-family: monospace;
      white-space: pre-wrap;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>[NEW CONSULTATION BOOKED]</h1>
    <p>A client has scheduled a technical briefing session. Details below:</p>
    <table>
      <tr>
        <td class="label">Client Name</td>
        <td class="val">{name}</td>
      </tr>
      <tr>
        <td class="label">Client Email</td>
        <td class="val">{email}</td>
      </tr>
      <tr>
        <td class="label">Date</td>
        <td class="val">{date}</td>
      </tr>
      <tr>
        <td class="label">Time</td>
        <td class="val">{time}</td>
      </tr>
      <tr>
        <td class="label">Solution Interest</td>
        <td class="val">{product}</td>
      </tr>
      <tr>
        <td class="label">Meeting Link</td>
        <td class="val"><a href="{meeting_url}" style="color:#00F2FE;">{meeting_url}</a></td>
      </tr>
      <tr>
        <td class="label">Reservation ID</td>
        <td class="val">GT-{reservation_id}</td>
      </tr>
    </table>
    
    <h2>Client Requirements / Notes:</h2>
    <div class="notes-box">{notes}</div>
  </div>
</body>
</html>
"""

def parse_dates(date_str, time_str):
    # Parses e.g. "June 25, 2026" and "10:00 AM" to datetime objects
    try:
        dt_str = f"{date_str} {time_str}"
        dt = datetime.strptime(dt_str, "%B %d, %Y %I:%M %p")
    except Exception:
        # Fallback to tomorrow
        dt = datetime.now() + timedelta(days=1)
        dt = dt.replace(hour=10, minute=0, second=0, microsecond=0)
    
    start_dt = dt
    end_dt = dt + timedelta(minutes=45)
    return start_dt, end_dt

def generate_ics(name, email, product, notes, start_dt, end_dt, meeting_url, reservation_id, smtp_user):
    # Generates a standard .ics VCalendar string
    now_str = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    start_str = start_dt.strftime("%Y%m%dT%H%M%SZ")
    end_str = end_dt.strftime("%Y%m%dT%H%M%SZ")
    
    organizer = f'ORGANIZER;CN="GianTecH Empire Team":mailto:{smtp_user if smtp_user else "support@giantech.app"}'
    escaped_notes = notes.replace('\n', '\\n')
    
    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//GianTecH Empire//Consultation Scheduler//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:REQUEST",
        "BEGIN:VEVENT",
        f"UID:booking_{reservation_id}@giantech.app",
        f"DTSTAMP:{now_str}",
        f"DTSTART:{start_str}",
        f"DTEND:{end_str}",
        f"SUMMARY:GianTecH Consultation: {product}",
        f"DESCRIPTION:Hello {name},\\n\\nYour technical consultation with GianTecH Empire is confirmed.\\n\\nMeeting Link: {meeting_url}\\n\\nClient Notes: {escaped_notes}",
        f"LOCATION:{meeting_url}",
        organizer,
        f'ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=NEEDS-ACTION;RSVP=TRUE;CN="{name}":mailto:{email if email else "client@giantech.app"}',
        "STATUS:CONFIRMED",
        "SEQUENCE:0",
        "END:VEVENT",
        "END:VCALENDAR"
    ]
    return "\r\n".join(ics_lines)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/book':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                name = data.get('name', 'Valued Client')
                email = data.get('email', '')
                product = data.get('product', 'General Consultation')
                notes = data.get('notes', 'No specific notes provided.')
                date = data.get('date', 'TBD')
                time = data.get('time', 'TBD')
                
                # Generate unique reservation ID
                import random
                reservation_id = f"{random.randint(100000, 999999)}"
                
                # Meeting coordinates
                meeting_url = f"https://meet.google.com/gt-consult-{name.lower().replace(' ', '-')[:8]}"
                
                # Setup dates
                start_dt, end_dt = parse_dates(date, time)
                start_iso = start_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                end_iso = end_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                dates_str = f"{start_dt.strftime('%Y%m%dT%H%M%SZ')}/{end_dt.strftime('%Y%m%dT%H%M%SZ')}"
                
                # Google Calendar link (fallback)
                cal_title = urllib.parse.quote(f"GianTecH Empire - {product}")
                cal_details = urllib.parse.quote(f"Consultation with GianTecH Empire. Join Meet: {meeting_url}")
                calendar_url = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={cal_title}&dates={dates_str}&details={cal_details}&location={urllib.parse.quote(meeting_url)}"
                
                # Notes section formatting
                if notes and notes.strip() != 'No specific notes provided.':
                    notes_section = f'<div class="section-title">Client Requirements & Notes</div><div class="details-box" style="font-family: monospace; white-space: pre-wrap; font-size: 13px; color: #d1d2d5; border: 1px solid #1f2023; background: #0c0d0e; padding: 15px;">{notes.replace(chr(10), "<br>")}</div>'
                else:
                    notes_section = ''
                
                # Render email body
                current_year = datetime.now().year
                html_email = EMAIL_TEMPLATE.format(
                    name=name,
                    date=date,
                    time=time,
                    product=product,
                    meeting_url=meeting_url,
                    calendar_url=calendar_url,
                    reservation_id=reservation_id,
                    iso_start=start_iso,
                    iso_end=end_iso,
                    notes_section=notes_section,
                    current_year=current_year
                )
                
                # Render host notification email
                html_host_email = HOST_EMAIL_TEMPLATE.format(
                    name=name,
                    email=email,
                    date=date,
                    time=time,
                    product=product,
                    meeting_url=meeting_url,
                    reservation_id=reservation_id,
                    notes=notes
                )
                
                # Save previews locally
                os.makedirs("sent_emails", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Save HTML preview
                preview_filename = f"sent_emails/booking_{timestamp}.html"
                with open(preview_filename, "w", encoding="utf-8") as f:
                    f.write(html_email)
                
                # Generate and save ICS file
                smtp_user = os.environ.get("SMTP_USER", "support@giantech.app")
                ics_content = generate_ics(name, email, product, notes, start_dt, end_dt, meeting_url, reservation_id, smtp_user)
                ics_filename = f"sent_emails/invite_{timestamp}.ics"
                with open(ics_filename, "wb") as f:
                    f.write(ics_content.encode('utf-8'))
                
                # Try sending real email if SMTP configured
                smtp_sent = False
                smtp_error = ""
                smtp_server = os.environ.get("SMTP_SERVER")
                smtp_port = os.environ.get("SMTP_PORT", "587")
                smtp_password = os.environ.get("SMTP_PASSWORD")
                host_email = "tchuekrostand@gmail.com"
                
                if smtp_server and smtp_user and smtp_password:
                    try:
                        # Establish SMTP connection
                        server = smtplib.SMTP(smtp_server, int(smtp_port))
                        server.starttls()
                        server.login(smtp_user, smtp_password)
                        
                        # 1. Send confirmation with invite.ics attachment to client (if email provided)
                        if email:
                            msg_client = MIMEMultipart("mixed")
                            msg_client["Subject"] = f"Confirmed: GianTecH Empire Consultation - GT-{reservation_id}"
                            msg_client["From"] = f"GianTecH Empire <{smtp_user}>"
                            msg_client["To"] = email
                            
                            # HTML content part
                            html_part = MIMEText(html_email, "html")
                            msg_client.attach(html_part)
                            
                            # Calendar invitation attachment (.ics)
                            ics_part = MIMEBase("text", "calendar", method="REQUEST", name="invite.ics")
                            ics_part.set_payload(ics_content.encode('utf-8'))
                            ics_part.add_header("Content-Disposition", "attachment", filename="invite.ics")
                            ics_part.add_header("Content-Class", "urn:content-classes:calendarmessage")
                            encoders.encode_base64(ics_part)
                            msg_client.attach(ics_part)
                            
                            server.sendmail(smtp_user, email, msg_client.as_string())
                            print(f"[SMTP] Sent confirmation email with invite.ics to client: {email}")
                            
                        # 2. Send notification to the host (tchuekrostand@gmail.com)
                        msg_host = MIMEMultipart("mixed")
                        msg_host["Subject"] = f"[NEW BOOKING] GT-{reservation_id} - {name} - {product}"
                        msg_host["From"] = f"GianTecH Empire Booking <{smtp_user}>"
                        msg_host["To"] = host_email
                        
                        html_host_part = MIMEText(html_host_email, "html")
                        msg_host.attach(html_host_part)
                        
                        # Attach ICS to host invitation as well
                        ics_host_part = MIMEBase("text", "calendar", method="REQUEST", name="invite.ics")
                        ics_host_part.set_payload(ics_content.encode('utf-8'))
                        ics_host_part.add_header("Content-Disposition", "attachment", filename="invite.ics")
                        encoders.encode_base64(ics_host_part)
                        msg_host.attach(ics_host_part)
                        
                        server.sendmail(smtp_user, host_email, msg_host.as_string())
                        print(f"[SMTP] Sent notification email with invite.ics to host: {host_email}")
                        
                        server.quit()
                        smtp_sent = True
                    except Exception as e:
                        smtp_error = str(e)
                        print(f"[SMTP ERROR] Failed to send email: {e}")
                
                # Send JSON response back to page
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {
                    "status": "success",
                    "meeting_url": meeting_url,
                    "email_preview": f"/{preview_filename}",
                    "ics_preview": f"/{ics_filename}",
                    "smtp_sent": smtp_sent,
                    "smtp_error": smtp_error
                }
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
                print(f"\\n[BOOKING CONFIRMED] Name: {name}, Email: {email}, Slot: {date} at {time}")
                print(f"[PREVIEW GENERATED] HTML Email: {os.path.abspath(preview_filename)}")
                print(f"[PREVIEW GENERATED] Calendar Invite: {os.path.abspath(ics_filename)}\\n")
                
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error processing booking: {e}".encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

# Start HTTP server
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(('', PORT), CustomHandler)
    print(f"GianTecH Custom server running on http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\\nServer stopped.")
