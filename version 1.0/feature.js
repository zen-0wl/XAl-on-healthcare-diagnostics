function showReport(reportId, insightId) {
    var reports = document.querySelectorAll('.content');
    var insights = document.querySelectorAll('.insights');
    reports.forEach(report => report.style.display = 'none');
    insights.forEach(insight => insight.style.display = 'none');
    document.getElementById(reportId).style.display = 'block';
    document.getElementById(insightId).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', () => {
    var contents = document.querySelectorAll('.content');
    contents.forEach(content => content.style.display = 'none');
});