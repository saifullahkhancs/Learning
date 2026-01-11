using chatbot.Application.Interfaces;
using chatbot.Application.UseCases.Users;
using chatbot.Infrastructure.Repositories;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Dependency Injection
builder.Services.AddSingleton<IUserRepository, InMemoryUserRepository>();
builder.Services.AddScoped<CreateUser>();
builder.Services.AddScoped<GetUsers>();
builder.Services.AddScoped<UpdateUser>();
builder.Services.AddScoped<DeleteUser>();

var app = builder.Build();
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapControllers();
app.Run();
