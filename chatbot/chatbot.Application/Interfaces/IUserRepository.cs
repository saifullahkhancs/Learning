using chatbot.Domain.Entities;

namespace chatbot.Application.Interfaces;

public interface IUserRepository
{
    Task AddAsync(User user);
    Task<List<User>> GetAllAsync();
    Task UpdateAsync(User user);
    Task DeleteAsync(Guid id);
}
