from odoo import models, fields, api
import nexmo
import requests
from twilio.rest import Client

class WizardSMS(models.TransientModel):
    _name = 'message.sms'
    _description = "Wizard: Quick Registration"

    service = fields.Selection(
        string="Type Service",
        selection=[("bulksms", "Bulksms"), ("vonage", "Vonage"), ("twilio", "Twilio")],
        required=True
    )
    remarque = fields.Text(String="Remarque")
    destinateur = fields.Char(String="Number Phone", required=True)
    sms = fields.Char(String="SMS", required=True)

    @api.onchange("service")
    def _onchange_service(self):
        if self.service == 'bulksms':
            self.remarque = 'exemple numéro : 06--------'
        if self.service == 'vonage':
            self.remarque = 'exemple numéro : 2126--------'
        if self.service == 'twilio':
            self.remarque = 'exemple numéro : +2126--------'

    #SMS
    def sms_odoo(self):
        #Bulksms
        if self.service == 'bulksms':
            data = {
                'token': 'MbLp0nNmJpHFoL7H7dc369Cm4',
                'tel': self.destinateur,
                'message': self.sms
            }
            response = requests.post('https://bulksms.ma/developer/sms/send', data=data)
            print(response)

        #Vonage(Nexmo)
        if self.service == 'vonage':
            client = nexmo.Client(key='a82ad853', secret='hifJZK3F4qgSota5')
            client.send_message({
                'from': 'Vonage APIs',
                'to': self.destinateur,
                'text': self.sms,
            })
            print(client)

        #Twilio
        if self.service == 'twilio':
            # SID from twilio.com/console
            account_sid = "AC4da836e95a4209043b28a47f18ed477f"
            # Your Auth Token from twilio.com/console
            auth_token = "7b9e0a8ed33efdf44861c67ac45e7000"

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to=self.destinateur,
                from_="+12514519781",
                body=self.sms)
            print(message.sid)