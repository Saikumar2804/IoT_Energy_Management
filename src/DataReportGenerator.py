class DataReportGenerator:
    def export_to_csv(self, data, output_path):
        data.to_csv(output_path, index=False)
        print(f"Report saved to {output_path}.")
