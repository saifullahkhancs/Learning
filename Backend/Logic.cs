What is dofferent between add and append in the lists in the c#?
Why append not work but add work??

_dbContext.service.Include(x=>x.branch_services).thenInclude(branch)  we can use that instead of texting Include _dbContext.service.Include("branch_service.branch")