from django import forms
from onl_lbmg_systemapp.models import Author, Book, BorrowRecord

class AuthorForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'email', 'bio']
    
    #Email Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ['@gmail.com', '@yahoo.com', '@outlook.com']
        if not any(email.endswith(domain) for domain in allowed_domains):
            raise forms.ValidationError("Only Gmail, Yahoo, or Outlook addresses are allowed.")
        return email    

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']
    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) #calendar date picker: <input type="date"> 

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']
    borrow_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))