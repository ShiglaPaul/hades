from msilib.schema import ListView
#from urllib import request
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from core.erp.forms import CategoryForm
#admin 123
from core.erp.models import *
# Create your views here.
def category_list(request):
    data={
        'title':'Listado de categorias',
        'categories': Category.objects.all()
    }

    return render(request,'category/list.html',data)

#Vistas basadas en clases
class CategoryListView(ListView):
    model=Category
    template_name='category/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        data={}
        #print('del post3')
        #print(request.POST)#trae el valor de post
        try:
            #data=Category.objects.get(pk=request.POST['id']).toJSON()
            #data['name']=cat.name
            #print(data)
            action=request.POST['action']
            if action=='searchdata':
                data=[]
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error']='ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    #En la variable q va los datos por defecto es en object_list
#sobre el metodo de query set
    '''def get_queryset(self):
        return Category.objects.filter(name__startswith='L')'''

    #get_context_data: devolvera valores adicionales
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Listado de categorias'
        context['create_url']=reverse_lazy('erp:category_create')
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        #context['object_list']=Product.objects.all()#sobreescribiendo el valor por defecto de object list   
        print(context)
        print('presentando ruta')
        print(reverse_lazy('erp:category_list'))
        return context

class CategoryCreateView(CreateView):
    model=Category#el modelo con el q voy a interactuar
    form_class=CategoryForm#el formulario con el q voy a trabajar
    template_name='category/create.html'#mi plantilla
    success_url=reverse_lazy('erp:category_list')#una vez creado, redirecciona a otra pagina
    
    '''def post(self, request,*args,**kwargs):
        print(request.POST)#que envia mi post
        form=CategoryForm(request.POST)#llamamos al formulario y enviamos ko q llega en post
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)#redirecciona una url
        self.object=None
        print(form.errors)#caso q haya error, imprime esto
        context=self.get_context_data(**kwargs)
        context['form']=form
        return render(request,self.template_name,context)'''
    def post(self,request,*args,**kwargs):
        data={}
        #print('del post3')
        #print(request.POST)#trae el valor de post
        try:
            action=request.POST['action']
            if action=='add':
                #pass
                #form=CategoryForm(request.POST)#contenemos nuestro formulario mediante form, pasamos los datos mediante esta variable request.POST
                form=self.get_form()#tambien obtenemos el formulrio
                '''if form.is_valid():
                    form.save()
                else:
                    data['error']=form.errors'''
                data=form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Crear una categoria'
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        context['action']='add'
        #context['object_list']=Product.objects.all()#sobreescribiendo el valor por defecto de object list   
        print(context)
        
        return context
class CategoryUpdateView(UpdateView):
    model=Category#el modelo con el q voy a interactuar
    form_class=CategoryForm#el formulario con el q voy a trabajar
    template_name='category/create.html'#mi plantilla
    success_url=reverse_lazy('erp:category_list')#una vez creado, redirecciona a otra pagina
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        data={}
        #print('del post3')
        #print(request.POST)#trae el valor de post
        try:
            action=request.POST['action']
            if action=='edit':
                #pass
                #form=CategoryForm(request.POST)#contenemos nuestro formulario mediante form, pasamos los datos mediante esta variable request.POST
                form=self.get_form()#tambien obtenemos el formulrio
                '''if form.is_valid():
                    form.save()
                else:
                    data['error']=form.errors'''
                data=form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.object)#en la variable self objects viene el valor
        print('mostrando object')
        print(self.get_object())
        print('mostrando context data')
        context=super().get_context_data(**kwargs)
        context['title']='Edicion una categoria'
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        context['action']='edit'
        #context['object_list']=Product.objects.all()#sobreescribiendo el valor por defecto de object list   
        print(context)
        return context
    
class CategoryDeleteView(DeleteView):
    model=Category
    template_name='category/delete.html'
    success_url=reverse_lazy('erp:category_list')#para retornar una vez q haya sido eliminado exitosamente
    
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data={}
        try:
            self.object.delete()
        except Exception as e:
            data['error']=str(e)        
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        '''print(self.object)#en la variable self objects viene el valor
        print('mostrando object')
        print(self.get_object())
        print('mostrando context data')'''     
        context=super().get_context_data(**kwargs)
        context['title']='Eliminacion de una categoria'
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        context['action']='delete'
        #context['object_list']=Product.objects.all()#sobreescribiendo el valor por defecto de object list   
        print(context)
        return context
class CategoryFormView(FormView):
    form_class=CategoryForm#el formulario con el q va ha trabajar
    template_name='category/create.html'#el template con el q va ha trabajar
    success_url=reverse_lazy('erp:category_list')#va ha retornar cuando se ejecute correctamente
    def form_valid(self, form):#cuando el formulario se ejecuta correctamente
        print(form.is_valid())
        print(form)
        return super().form_valid(form)
    def form_invalid(self, form):#para ver los errores
        print(form.errors)#verifico el error
        print(form.is_valid())#true si es valido o falso caso contrario
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Form categoria'
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        #context['object_list']=Product.objects.all()#sobreescribiendo el valor por defecto de object list   
        context['action']='add'
        return context
