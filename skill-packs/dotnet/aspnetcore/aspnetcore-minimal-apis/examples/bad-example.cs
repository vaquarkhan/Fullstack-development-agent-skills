// BAD — anonymous object, no auth, sync blocking
app.MapPost("/orders", (HttpContext ctx) =>
{
    var body = ctx.Request.ReadFromJsonAsync<object>().Result;
    return new { ok = true, data = body };
});
