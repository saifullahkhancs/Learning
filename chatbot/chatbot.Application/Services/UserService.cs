using chatbot.Application.Interfaces;
using chatbot.Domain.Entities;

namespace chatbot.Application.UseCases.Users;

public class CreateUser
{
    private readonly IUserRepository _repo;

    public CreateUser(IUserRepository repo)
    {
        _repo = repo;
    }

    public async Task Execute(string name, string email)
    {
        var user = new User
        {
            Id = Guid.NewGuid(),
            Name = name,
            Email = email
        };

        await _repo.AddAsync(user);
    }
}

public class GetUsers
{
    private readonly IUserRepository _repo;

    public GetUsers(IUserRepository repo)
    {
        _repo = repo;
    }

    public List<User> Execute()
    {
        return _repo.GetAll();
    }
}

public class UpdateUser
{
    private readonly IUserRepository _repo;

    public UpdateUser(IUserRepository repo)
    {
        _repo = repo;
    }

    public async Task Execute(User user)
    {
        await _repo.UpdateAsync(user);
    }
}

public class DeleteUser
{
    private readonly IUserRepository _repo;

    public DeleteUser(IUserRepository repo)
    {
        _repo = repo;
    }

    public async Task Execute(Guid id)
    {
        await _repo.DeleteAsync(id);
    }
}
