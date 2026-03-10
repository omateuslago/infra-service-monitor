namespace InfraMonitorAPI.Models
{
    public class Service
    {
        public int Id { get; set; }
        public required string Name { get; set; }
        public required string Url { get; set; }
        public bool IsActive { get; set; }
    }
}
