using System;
using System.Reactive;
using System.Reactive.Linq;
using System.Windows.Input;
using Avalonia.Controls;
using ReactiveUI;

public class MainViewModel : ReactiveObject
{
    private string _imageAPath = "departure_A.png";
    private string _imageBPath = "departure_B.png";
    private bool _isImageAVisible = true;

    public string ImageAPath
    {
        get => _imageAPath;
        set => this.RaiseAndSetIfChanged(ref _imageAPath, value);
    }

    public string ImageBPath
    {
        get => _imageBPath;
        set => this.RaiseAndSetIfChanged(ref _imageBPath, value);
    }

    public bool IsImageAVisible
    {
        get => _isImageAVisible;
        set => this.RaiseAndSetIfChanged(ref _isImageAVisible, value);
    }

    public ICommand ToggleImagesCommand { get; }

    public MainViewModel()
    {
        ToggleImagesCommand = ReactiveCommand.Create(ToggleImages);
    }

    private void ToggleImages()
    {
        IsImageAVisible = !IsImageAVisible;
    }
}
