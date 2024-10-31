from django import forms

class JsonFileUpload(forms.Form):

    jsonFile = forms.FileField(required=True, widget=forms.TextInput(attrs={"name":"jsonFile" ,"class":"form-control", "type":"file", "id":"formFile"}))

#render html form by parsing uploaded json file
def dyFrmBuilder (json_data):

    class DynamicForm(forms.Form):
        pass
    #parsing Field members
    for field in json_data["fields"]:
            name = field["name"]
            label = field["text"]
            type = field["type"]
            choices = field["choices"] if "choices" in field else []
            required = field["required"] if "required" in field else ""
            fclass = field["class"] if "class" in field else ""
            fid = field["id"] if "id" in field else ""

            if (field["type"] == "text" or field["type"] =="CharField"):
                inst = forms.CharField(label=label, required=required) #make an instance of field

            elif field["type"] == "IntegerField":
                inst = forms.IntegerField(label=label, required=required)

            elif (field["type"] == "ChoiceField") and choices:
                inst = forms.ChoiceField(label=label, choices=choices, required=required)
            
            elif field["type"] == "BooleanField":
                inst = forms.BooleanField(label=label, required=required)

            elif (field["type"] == "DateField") or ((field["type"] == "date")):
                inst = forms.DateField(label=label, required=required)
            
            elif (field["type"] == "EmailField") or (field["type"] == "email"):
                inst = forms.EmailField(label=label, required=required, initial="email@example.com")
            
            elif field["type"] == "password":
                inst = forms.CharField(widget=forms.PasswordInput, required=required, label=label)
                        
            else: 
                continue
            #make a django form with instances which we create during parsing
            DynamicForm.base_fields[name] = inst

    return DynamicForm #return django form
