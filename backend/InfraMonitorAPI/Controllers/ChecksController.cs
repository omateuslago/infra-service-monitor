using Microsoft.AspNetCore.Mvc;
using InfraMonitorAPI.Database;
using InfraMonitorAPI.Models;

namespace InfraMonitorAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ChecksController : ControllerBase
    {
        private readonly AppDbContext _context;

        public ChecksController(AppDbContext context)
        {
            _context = context;
        }
       
        [HttpPost]
        public IActionResult Add(ServiceCheck check)
        {
            _context.ServiceChecks.Add(check);
            _context.SaveChanges();

            return Ok(check);
        }
    }
}