using chatbot.Application.UseCases.Users;
using chatbot.Domain.Entities;
using Microsoft.AspNetCore.Mvc;

namespace chatbot.Api.Controllers;

[ApiController]
[Route("api/users")]
public class UsersController : ControllerBase
{
    private readonly CreateUser _create;
    private readonly GetUsers _get;
    private readonly UpdateUser _update;
    private readonly DeleteUser _delete;

    public UsersController(
        CreateUser create,
        GetUsers get,
        UpdateUser update,
        DeleteUser delete)
    {
        _create = create;
        _get = get;
        _update = update;
        _delete = delete;
    }

    [HttpPost]
    public async Task<IActionResult> Create(User user)
    {
        await _create.Execute(user.Name, user.Email);
        return Ok();
    }

    [HttpGet]
    public IActionResult Get()
    {
        return Ok(_get.Execute());
    }

    [HttpPut]
    public async Task<IActionResult> Update(User user)
    {
        try
        {
            await _update.Execute(user);
            return Ok();
        }
        catch (ArgumentException ex)
        {
            return NotFound(ex.Message);
        }
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete(Guid id)
    {
        await _delete.Execute(id);
        return Ok();
    }
}
