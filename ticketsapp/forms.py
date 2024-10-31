from django import forms
from servicesapp.models import ServiceModel


def frmBuilder (json_data):
    class IssueTicketForm(forms.Form):
        for field in json_data["fields"]:
            name = field["name"]
            label = field["text"]

            if field["type"] == "text":
                locals()[name] = forms.CharField(label=label, required= True)

            elif field["type"] == "select":
                choices=[('','--------------')]
                if field.get("option") == 'db_base':
                    for title in ServiceModel.objects.all():
                        choices.append((title.id, title.name))
                        locals()[name] = forms.ChoiceField(label=label, choices=choices,initial='', required=True)
                        
                else: 
                    choices=[('','--------------')]
                    for option in field["option"]:
                        choices.append((int(option["value"]), option["text"]))
                        locals()[name] = forms.ChoiceField(label=label, choices=choices,initial='', required=True)   
    return IssueTicketForm