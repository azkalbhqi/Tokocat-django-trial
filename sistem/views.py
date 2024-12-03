from django.shortcuts import render, get_object_or_404, redirect
from .models import Paint
from .forms import PaintForm


# sistem/views.py

def home(request):
    return render(request, 'sistem/home.html')  # 'sistem/home.html' matches the folder structure


# List all paints
def paint_list(request):
    paints = Paint.objects.all()
    return render(request, 'sistem/paint_list.html', {'paints': paints})

# Create a new paint product
def create_paint(request):
    if request.method == 'POST':
        form = PaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paint_list')
    else:
        form = PaintForm()
    return render(request, 'sistem/create_paint.html', {'form': form})

# Update an existing paint product
def update_paint(request, pk):
    paint = get_object_or_404(Paint, pk=pk)
    if request.method == 'POST':
        form = PaintForm(request.POST, instance=paint)
        if form.is_valid():
            form.save()
            return redirect('paint_list')
    else:
        form = PaintForm(instance=paint)
    return render(request, 'sistem/update_paint.html', {'form': form})

# Delete a paint product
def delete_paint(request, pk):
    paint = get_object_or_404(Paint, pk=pk)
    if request.method == 'POST':
        paint.delete()
        return redirect('paint_list')
    return render(request, 'sistem/delete_paint.html', {'paint': paint})
