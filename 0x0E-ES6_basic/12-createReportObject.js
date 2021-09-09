export default function createReportObject(employeesList) {
  const allEmployees = {};
  const entries = Object.entries(employeesList);
  for (const [k, v] of entries) {
    allEmployees[`${k}`] = v;
  };

  const obj = { allEmployees, getNumberOfDepartments: (employeesList) => Object.keys(employeesList).length };
}

return obj;
