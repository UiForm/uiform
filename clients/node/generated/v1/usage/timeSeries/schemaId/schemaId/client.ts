import { AbstractClient, CompositionClient, streamResponse } from '@/client';
import { TimeRange, UsageTimeSeries } from "@/types";

export default class APISchemaId extends CompositionClient {
  constructor(client: AbstractClient) {
    super(client);
  }


  async get(schemaId: string, { timeRange }: { timeRange: TimeRange }): Promise<UsageTimeSeries> {
    let res = await this._fetch({
      url: `/v1/usage/time_series/schema_id/${schemaId}`,
      method: "GET",
      params: { "time_range": timeRange },
      auth: ["HTTPBearer", "Master Key", "API Key", "Outlook Auth"],
    });
    if (res.headers.get("Content-Type") === "application/json") return res.json();
    throw new Error("Bad content type");
  }
  
}
