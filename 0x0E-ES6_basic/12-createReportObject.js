export default function createReportObject(employeesList) {
  const entries = Object.entries(employeesList)
  for (const [k, v] of entries) {
    const allEmployees[`${k}`] = v;
  };

  return { allEmployees, getNumberOfDepartments: (employeesList) => Object.keys(employeesList).length };
}
