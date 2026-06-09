from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <div style="font-family: Arial, sans-serif; max-width: 650px; margin: 40px auto; padding: 30px; border: 1px solid #e0e0e0; border-radius: 12px; box-shadow: 0px 4px 20px rgba(0,0,0,0.08); background-color: #ffffff;">
        <h1 style="color: #2c3e50; margin-bottom: 5px; font-size: 26px;">Welcome to My Professional Portfolio</h1>
        <p style="font-size: 14px; color: #7f8c8d; margin-top: 0;">This application is running locally on a custom Python server.</p>
        
        <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
        
        <!-- Profile Header -->
        <p style="font-size: 22px; font-weight: bold; color: #16a085; margin-bottom: 5px;">Nathalie Abril (Margarete)</p>
        <p style="font-size: 16px; font-weight: bold; color: #2980b9; margin-top: 0; margin-bottom: 15px;">Business Management Graduate & Aspiring Developer</p>
        
        <p style="font-size: 15px; color: #34495e; line-height: 1.6; margin-bottom: 25px;">
            Leveraging a Bachelor's degree in Management from Holy Angel University alongside hands-on experience in client services, marketing operations, and administrative coordination to build value-driven software solutions.
        </p>

        <!-- Dynamic Skills Grid -->
        <div style="display: flex; gap: 20px; justify-content: space-between; background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 25px;">
            <div style="width: 48%;">
                <h3 style="color: #2c3e50; margin-top: 0; font-size: 15px;">💼 Business Expertise</h3>
                <ul style="font-size: 13px; color: #555; padding-left: 18px; margin: 0; line-height: 1.6;">
                    <li>Marketing & Advertising Strategy</li>
                    <li>Client Service Coordination</li>
                    <li>Operations & Management</li>
                </ul>
            </div>
            <div style="width: 48%;">
                <h3 style="color: #2c3e50; margin-top: 0; font-size: 15px;">💻 Technical Skills</h3>
                <ul style="font-size: 13px; color: #555; padding-left: 18px; margin: 0; line-height: 1.6;">
                    <li>Python Core & Scripting</li>
                    <li>Web Backend (Flask Servers)</li>
                    <li>HTML / CSS Interface Layouts</li>
                </ul>
            </div>
        </div>

        <!-- Software Development Projects Section -->
        <h3 style="color: #2c3e50; font-size: 18px; margin-top: 30px; margin-bottom: 15px;">🛠️ Technical Projects</h3>
        
        <!-- Project Card 1 -->
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; margin-bottom: 15px; background-color: #ffffff; transition: 0.3s;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <strong style="color: #2c3e50; font-size: 16px;">Personal Web Portfolio Server</strong>
                <span style="font-size: 11px; background-color: #e2f0d9; color: #385723; padding: 3px 8px; border-radius: 12px; font-weight: bold;">Python & Flask</span>
            </div>
            <p style="font-size: 13px; color: #555; margin: 0; line-height: 1.5;">
                Developed a local web server interface to serve interactive resume content. Configured network routes, customized frontend HTML layout properties, and established environment controls.
            </p>
        </div>

        <!-- Placeholder for Project 2 -->
        <div style="border: 1px dashed #cbd5e1; border-radius: 8px; padding: 15px; background-color: #f8fafc; text-align: center;">
            <p style="font-size: 13px; color: #94a3b8; margin: 0; font-style: italic;">
                [ Project #2: Incoming Business Automation Script / Data Dashboard ]
            </p>
        </div>

    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
