var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddAuthentication().AddJwtBearer();
builder.Services.AddAuthorization();
builder.Services.AddScoped<IOrderService, OrderService>();

var app = builder.Build();
app.UseAuthentication();
app.UseAuthorization();
// Map endpoints here
app.Run();
