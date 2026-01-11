using chatbot.Application.Interfaces;

using chatbot.Domain.Entities;

namespace chatbot.Infrastructure.Repositories;

public class InMemoryUserRepository : IUserRepository
{
    private static readonly List<User> _users = new();

    public Task AddAsync(User user)
    {
        _users.Add(user);
        return Task.CompletedTask;
    }

    public List<User> GetAll() => _users;

    public Task UpdateAsync(User user)
    {
        var existing = _users.FirstOrDefault(x => x.Id == user.Id);
        if (existing == null)
        {
            throw new ArgumentException($"User with id {user.Id} not found");
        }
        existing.Name = user.Name;
        existing.Email = user.Email;
        return Task.CompletedTask;
    }

    public Task DeleteAsync(Guid id)
    {
        var user = _users.FirstOrDefault(x => x.Id == id);

        if (user == null)
            return Task.CompletedTask;

        _users.Remove(user);
        return Task.CompletedTask;
    }
}
