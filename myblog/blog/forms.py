from django.forms import ModelForm, Textarea
from blog.models import Comment
from django.utils.translation import gettext_lazy as _


class UserCommentModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserCommentModelForm, self).__init__(*args, **kwargs)
        
        # Removing the default label suffix
        self.label_suffix = ''

    
    
    def clean_comment(self):
        data = self.cleaned_data['comment']

        # No valdiation for now

        # Return clean data
        return data


    
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment':_("Comment")}
        help_texts = {'comments':_("Please give your comment")}
        widgets={'comment':Textarea(attrs={'placeholder':"Leave a comment here", 'class':'form-control'})}
        



